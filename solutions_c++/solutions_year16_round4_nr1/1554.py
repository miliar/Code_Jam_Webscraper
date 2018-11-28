#include<iostream>
#include<vector>

using namespace std;

int p, r, s, n;
int N[3];

struct node
{
    node *l, *r;
    int c;
    vector<int> V;
    
    node() {l = r = NULL;}
    node(int x) {c = x, l = r = NULL;}
    ~node() {delete l, delete r;}
};

node* create(int c, int k)
{
	if (k == 0)
	{
		N[c]--;
		return new node(c);
	}
	node* X = new node(c);
	if (c == 0)
	{
		X->l = create(1, k - 1);
		X->r = create(2, k - 1);
	}
	if (c == 1)
	{
		X->l = create(0, k - 1);
		X->r = create(2, k - 1);
	}
	if (c == 2)
	{
		X->l = create(0, k - 1);
		X->r = create(1, k - 1);
	}
	return X;
}

string S = "";

void solve(node* X, int k)
{
	if (k == 0)
	{
		X->V.push_back(X->c);
		return;
	}
	node *l = X->l, *r = X->r;
	solve(l, k - 1);
	solve(r, k - 1);
	for (int i = 0; i < l->V.size(); i++)
		X->V.push_back(min(l->V[i], r->V[i]));
		
	int y;
	if (l->V.back() == 0 and r->V.back() == 1) y = 0;
	if (l->V.back() == 0 and r->V.back() == 2) y = 1;
	if (l->V.back() == 1 and r->V.back() == 2) y = 2;
	X->V.push_back(y);

	for (int i = 0; i < l->V.size(); i++)
		if (l->V[i] > r->V[i])
		{
			swap(X->l, X->r);
			break;
		}
}

void read(node* X, int k)
{
	if (k == 0)
	{
		char c;
		if (X->c == 0) c = 'P';
		else if (X->c == 1) c = 'R';
		else c = 'S';
		S += c;
		return;
	}
	read(X->l, k - 1);
	read(X->r, k - 1);
}

string ans[3];

string mn()
{
	string x = ans[0];
	if (ans[1] < x) x = ans[1];
	if (ans[2] < x) x = ans[2];
	return x;
}

int main()
{
    ios_base::sync_with_stdio(0);
    int tt;
    cin >> tt;
    for (int t = 1; t <= tt; t++)
    {
        int p0, r0, s0;
        cin >> n >> r0 >> p0 >> s0;
        
        for (int i = 0; i < 3; i++)
        {
	        N[0] = p0, N[1] = r0, N[2] = s0;
        	node* root = create(i, n);
        	if (N[0] < 0 or N[1] < 0 or N[2] < 0)
        	{
        		delete root;
        		ans[i] = "Z";
        		continue;
        	}
        	S = "";
	        solve(root, n);
	        read(root, n);
	        delete root;
	        ans[i] = S;
        }
        string a = mn();
        cout << "Case #" << t << ": ";
        if (a == "Z") cout << "IMPOSSIBLE\n";
        else cout << a << "\n";
    }
    
    
    return 0;
}

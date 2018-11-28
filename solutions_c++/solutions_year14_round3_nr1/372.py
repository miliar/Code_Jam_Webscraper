#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <deque>
#include <stack>
#include <cmath>
#include <map>
#include <utility>
#include <set>
#include <algorithm>
using namespace std;

vector<string> v;

int fact(int x)
{
	int rez=1;
	for(int i=1;i<=x;++i)
		rez*=i;
	return rez;
}

bool Ok()
{
	for(int i=1;i<v.size();++i)
		if(v[i].front()!=v[i-1].back())
			return false;
	return true;
}


using namespace std;

inline long long gcd (long long a, long long b)
{
    while (b)
    {
        a %= b;
        swap (a,b);
    }
    return a;
}

long long mas [32];

int main ()
{
    ios_base::sync_with_stdio(false);
  freopen("D:\\in.txt","r",stdin);
freopen("D:\\out.txt","w",stdout);
    mas[0] = 1;
    for (int i = 1; i < 32; ++i)
    {
        mas[i] = mas[i - 1] * 2;
    }
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        cout << "Case #" << i + 1 << ": ";
        long long a,b;
        cin >> a;
        cin.clear();
        cin.get();
        cin >> b;
        long long temp = gcd (a,b);
        a /= temp;
        b /= temp;
        bool ok = false;
        for (int j = 0; j < 32; ++j)
        {
            if (b == mas[j])
                ok = true;
        }
        if (!ok || (a == 0))
        {
            cout << "impossible" << endl;
            continue;
        }

        for (int j = 0; j < 32; ++j)
        {
            if (static_cast <double> (a) / b >= 1.0 / mas[j])
            {
                cout << j << endl;
                break;
            }
        }

    }
}



//int main()
//{
//	//freopen("D:\\in.txt","r",stdin);
//	//freopen("D:\\out.txt","w",stdout);
//	int T;
//	cin>>T;
//	vector<string> v;
//	for(int i=0;i<T;++i)
//	{
//		int n;
//		cin>>n;
//		v.clear();
//		string s;
//		for(int i=0;i<n;++i)
//		{
//			cin>>s;
//			v.push_back(s);
//		}
//		int k=fact(n);
//		int rez=0;
//		for(int j=0;j<k;++j)
//		{
//			if(Ok())
//				++rez;
//			next_permutation(v.begin(),v.end());
//		}
//		cout<<"Case #"<<i+1<<": "<<rez<<endl;
//	}
//
//	
//
//
//	return 0;
//}
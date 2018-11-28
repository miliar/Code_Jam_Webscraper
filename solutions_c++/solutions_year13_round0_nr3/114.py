#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

void redirectIO()
{
	string fileName;
	cin >> fileName;
	string input = fileName + ".in";
	string output = fileName + ".out";

	freopen(input.c_str(), "r", stdin);
	freopen(output.c_str(), "w", stdout);
}

vector<string> res;
char v[64];

void dfs(int c, int d, int len, int sum)
{
	if (c == d)
	{
		for (int i = 0, j = len - 1; i < j; ++i, --j)
			v[j] = v[i];
		v[len] = '\0';
		res.push_back(v);
		return;
	}

	for (int i = c == 0; i <= 2; ++i)
		if (i * i * 2 <= sum)
		{
			v[c] = i + '0';
			dfs(c + 1, d, len, sum - i * i * 2);
		}
}

bool cmp(string a, string b)
{
	if (a.size() == b.size())
	{
		return a < b;
	}
	else
	{
		return a.size() < b.size();
	}
}

const int MaxL = 256;
struct BigNum{
    const static int Base = 10000;
    const static int W = 4;
    const static int numLen = MaxL / W;
    char ng;
    int d[numLen],L;
    BigNum(){ng = 0,d[L = 0] = 0;}
    BigNum(char *st){set(st);}
    BigNum(int n){set(n);}
    void set(const char *st){
        int len = strlen(st);
        ng = st[0] == '-';
        d[L = 0] = 0;
        for (int i = len-1;i >= ng;){
            int i0 = i-W+1;
            if (i0 < ng) i0 = ng;
            int &v = d[L++] = 0;
            for (int j = i0;j <= i;j++)
                v = v*10+st[j]-'0';
            i = i0-1;
        }
        adjust();
    }
    void set(int n){
        ng = n < 0;
        d[L = 0] = 0;
        while (n){
            d[L++] = n % Base;
            n /= Base;
        }
    }
    void out(){
        if (L == 0){
            putchar('0');
            return;
        }
        if (ng) putchar('-');
        printf("%d",d[L-1]);
        for (int i = L-2;i >= 0;i--)
            printf("%0*d",W,d[i]);
    }
    void adjust(){//be sure that len of result is not larger than L+1
        d[L] = 0;
        for (int i = 0;i < L;i++)
            if (d[i] >= Base){
                d[i+1] += d[i] / Base;
                d[i] %= Base;
            }else if (d[i] < 0){//only useful when sub
                --d[i+1];
                d[i] += Base;
            }
        L += d[L] != 0;
        while (L > 0 && d[L-1] == 0)
            --L;
        if (L == 0) ng = 0,d[0] = 0;
    }
    bool operator <(const BigNum &B){
        if (L == B.L){
            for (int i = L-1;i >= 0;i--)
                if (d[i] != B.d[i])
                    return d[i] < B.d[i];
        }
        return L < B.L;
    }
    BigNum operator <<(int x){
        if (x > numLen) x = numLen;
        BigNum r = *this;
        if (r.L == 0)
            return r;
        int mL = (x+L < numLen?x+L:numLen)-x;
        r.L = x+mL;
        memmove(r.d+x,r.d,sizeof(r.d[0])*mL);
        memset(r.d,0,sizeof(r.d[0])*x);
        return r;
    }
    BigNum operator >>(int x){
        BigNum r = *this;
        if (x >= L){
            r.d[r.L = 0] = 0;
            r.ng = 0;
            return r;
        }
        r.L -= x;
        memmove(d+x,d,sizeof(d[0])*r.L);
        return r;
    }
    BigNum operator +(const BigNum &B){
        BigNum r;
        r.ng = ng;
        r.L = L > B.L?L:B.L;
        int e = L < B.L?L:B.L;
        char sub = ng ^ B.ng;
        if (sub){
            for (int i = 0;i < e;i++)
                r.d[i] = d[i]-B.d[i];
            if (L > B.L)
                memcpy(r.d+e,d+e,sizeof(r.d[0])*(L-e));
            else if (L < B.L){
                memcpy(r.d+e,B.d+e,sizeof(r.d[0])*(B.L-e-1));
                r.d[B.L-1] = -B.d[B.L-1];
            }
            if (r.d[r.L-1] < 0){
                r.d[r.L-1] = -r.d[r.L-1];
                if (e < r.L) r.d[e-1] = -r.d[e-1];
                for (int i = 0;i+1 < e;i++)
                    r.d[i] = -r.d[i];
                r.ng ^= 1;
            }
        }else{
            for (int i = 0;i < e;i++)
                r.d[i] = d[i]+B.d[i];
            if (L > B.L)
                memcpy(r.d+e,d+e,sizeof(r.d[0])*(L-e));
            else if (L < B.L)
                memcpy(r.d+e,B.d+e,sizeof(r.d[0])*(B.L-e));
        }
        r.adjust();
        return r;
    }
    BigNum operator -(const BigNum &B){
        BigNum cB = B;
        cB.ng ^= 1;
        return (*this)+cB;
    }
    BigNum operator *(const BigNum &B){
        BigNum r;
        int &c = r.L = L+B.L-1;
        memset(r.d,0,sizeof(r.d[0])*c);
        for (int i = 0;i < B.L;i++)
            for (int j = 0;j < L;j++)
                r.d[i+j] += B.d[i]*d[j];
        r.ng = ng ^ B.ng;
        r.adjust();
        return r;
    }
    //b should be smaller than Base
    BigNum operator +(int &b){
        BigNum r = *this;
        if (L == 0){
            r.set(b);
            return r;
        }
        char bng = b < 0;
        char sub = r.ng ^ bng;
        if (b < 0) b = -b;
        r.d[0] += sub?-b:b;
        if (L == 1){
            if (r.d[0] == 0){
                r.d[r.L = 0] = 0;
                r.ng = 0;
            }else if (r.d[0] < 0){
                r.d[0] = -r.d[0];
                r.ng ^= 1;
            }
            return r;
        }
        r.adjust();
        return r;
    }
    BigNum operator -(int &b){
        int cb = -b;
        return (*this)+cb;
    }
    BigNum operator *(int &b){
        BigNum r;
        if (L == 0) return r;
        r.ng = ng;
        r.L = L;
        if (b < 0) b = -b,r.ng ^= 1;
        for (int j = 0;j < L;j++)
            r.d[j] = b*d[j];
        r.adjust();
        return r;
    }
    BigNum operator /(int &b){
        BigNum r;
        if (L == 0) return r;
        r.ng = ng;
        r.L = L;
        if (b < 0) b = -b,r.ng ^= 1;
        int rem = 0;//r % b
        for (int j = L-1;j >= 0;j--){
            int cd = d[j]+rem*Base;
            r.d[j] = cd / b;
            rem = cd % b;
        }
        r.adjust();
        return r;
    }
    BigNum sqrt(){
        BigNum U,r,D;
        for (int i = L;i > 0;){
            U = (U << 1)+d[--i];
            D = D << 1;
            if (i & 1){
                U = (U << 1)+d[--i];
                D = D << 1;
            }
            r = r << 1;
            int s = 0,t = Base+1;
            while (s+1 < t){
                int d = (s+t) >> 1;
                BigNum nD = D+r*(d*2)+BigNum(d*d);
                if (U < nD) t = d;
                else s = d;
            }
            D = D+r*(s*2)+BigNum(s*s);
            r = r+s;
        }
        return r;
    }
};

int Cal(BigNum& N)
{
	BigNum S = N.sqrt(), D;

	int s = -1, t = res.size();
	while (s + 1 < t)
	{
		int d = (s + t) / 2;
		D.set(res[d].c_str());
		if (S < D) t = d;
		else s = d;
	}

	//cout << "Query ";N.out();cout << ":" << s + 1 << endl;
	return s + 1;
}

int main()
{
	res.push_back("1");
	res.push_back("2");
	res.push_back("3");

	for (int i = 2; i <= 50; ++i)
	{
		int d = i / 2;

		if (i % 2 == 0)
		{
			dfs(0, d, i, 9);
		}
		else
		{
			for (int j = 0; j <= 2; ++j)
			{
				v[d] = j + '0'; dfs(0, d, i, 9 - j * j);
			}
		}
	}

	sort(res.begin(), res.end(), cmp);

	//for (int i = 0; i < res.size(); ++i) cout << res[i] << endl; cout << endl;
	//cout << res.size() << endl;
	//system("pause");

	redirectIO();
	
	BigNum One; One.set(1);

	int T;
	scanf("%d", &T);

	for (int ct = 1; ct <= T; ++ct)
	{
		BigNum A, B;
		string s;
		cin >> s; A.set(s.c_str());
		cin >> s; B.set(s.c_str());
		printf("Case #%d: ", ct);
		cout << Cal(B) - Cal(A - One) << endl;
	}
}
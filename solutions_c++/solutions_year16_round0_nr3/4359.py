#include <bits/stdc++.h>
using namespace std;
bool IsPrime(long long number,long long *d);
int main()
{
    freopen("in3.txt","r",stdin);
    freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	int c = 1;
	while(c<=t)
	{
		int n,j;
		cin>>n>>j;
		string s;
		vector<string> v;
		vector<vector<long long> > count;
		for(long long i=0;i<(1<<(n-2));i++)
		{
		        vector<long long> temp_c;
		        bool flag = true;
				s = "1";
				vector<char> ch(n-2,'0');
				int ch_ind = n-2-1;
				long long num = i;
				while(num)
				{
					if(ch_ind >= 0)
						ch[ch_ind--] = '0' + (num%2) ;
					else
						break;
					num /= 2;
				}
				string ss(ch.begin(),ch.end());
				s += ss;
				s += "1";
				//cout<<s<<endl;
				for(int b = 2;b<=10;b++)
				{
				        long long div;
						long long number = stol(s,nullptr,b);
						if(IsPrime(number,&div))
						{
						        temp_c.clear();
						        flag = false;
					            break;
						}
						else{
						        temp_c.push_back(div);
						        //cout<<div<<endl;
						}


				}

				if(flag)
				{
				        v.push_back(s);
				        count.push_back(temp_c);
		                if(v.size()==j)
		                    break;
				}

				s.clear();
				ch.clear();
		}
		cout<<"Case #"<<c<<":"<<endl;
		for(int k=0;k<j;k++)
		{
		    cout<<v[k]<<" ";
		    for(int l=0;l<9;l++)
		        cout<<count[k][l]<<" ";
		    cout<<endl;
		}
		c++;
	}
}
bool IsPrime(long long number,long long *d)
{
	long long i;

	for (i=2; i*i<=number; i++)
	{
		if (number % i == 0)
		{
		    *d = i;
			return false;
		}
	}

	return true;
}

  /*
Aditya R

*/
using namespace std;
#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<limits>
#include<cmath>
#include<map>
#define LLU long long unsigned int
#define LLD long long double
#define FOR(i,N) for(int i=0;i<(N);i++)
    int main()
    {
        int test, cno=0;
        cin>>test;
        while(test--)
        {
            cno++ ;
	    int n,nvalue=0,i,k,flag=0,flag2=0,j=0;
            string s;
	    cin>>s ;
            cin>>n ;

            for(i=0;i<s.length()-n+1;i++)
            {
	//	cout<<"i is "<<i<<endl;
		flag=0;
                for(k=0;k<n;k++)
                {
                    if(!(s[i+k]!='a'&&s[i+k]!='e'&&s[i+k]!='i'&&s[i+k]!='o'&&s[i+k]!='u' ) )
                    {

                        flag=1;
			break ;

                    }


                }
                if(!flag)
		{ 
			flag2=1;
	//		cout<<"found at "<<i<<endl;
	//		cout<<"value is "<<(i+1)<<"*"<<(s.length()-i-n+1)<<"="<<(i+1)*(s.length()-i-n+1)<<endl;
		        nvalue+=(i-j+1)*(s.length()-i-n+1);
			j=i+1;
		}
            }
	    cout<<"Case #"<<cno<<": "<<nvalue<<endl;
        }

    return 0 ;
    }


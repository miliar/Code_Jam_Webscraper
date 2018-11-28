#include<bits/stdc++.h>
#define mod 1000000007
#define SIZE 1000007
#define ll long long
#define INF LLONG_MAX
#define f(i,a,b) for(i=a;i<b;i++)
using namespace std;

typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

int main() {
    freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
    ios::sync_with_stdio(0);
    int tc,i,j,n;
	ll ans,total,len;
	string str,temp,temp1;
    cin>>tc;
    for(int t=1;t<=tc;t++){
        cin>>n;
        ll p[n];
        total = 0;
        f(i,0,n){
            cin>>p[i];
            total+=p[i];
        }
        cout<<"Case #"<<t<<": ";
        str="";
        f(i,0,n)
            f(j,0,p[i])
                str+=(char)(i+65);
		while(str.length()>3){
            len = str.length();
            for(i=0;i<len-1;i++){
                p[(int)str[i]-65]--;
                p[(int)str[i+1]-65]--;
                f(j,0,n)
                    if(p[j]>(len-2)/2)
                        break;
                if(j==n){
                    cout<<str[i]<<str[i+1]<<" ";
                    temp=str.substr(0,i);
                    temp1=str.substr(i+2,len-2-i);
                    str=temp+temp1;
                    break;
                }
                p[(int)str[i]-65]++;
                p[(int)str[i+1]-65]++;
            }
            if(i==len-1){
                for(i=0;i<n-1;i++){
                    for(j=i+1;j<n;j++)
                        if(p[i]>(len-2)/2&&p[j]>(len-2)/2)
                            break;
                    if(j<n) break;
                }
                p[i]--;
                p[j]--;
                cout<<(char)(i+65)<<(char)(j+65)<<" ";
                str.erase(str.find((char)(i+65)),1);
                str.erase(str.find((char)(j+65)),1);
            }
		}
        if(str.length()==3)
            cout<<str[0]<<" "<<str[1]<<str[2]<<" ";
        else if(str.length()==2)
            cout<<str[0]<<str[1]<<" ";
		cout<<"\n";
	}
	return 0;
}

/*
46
2
2 2
3
3 2 2
3
1 1 2
3
2 3 1
3
1 3 4
3
2 1 2
3
2 3 3
3
4 1 4
3
1 4 3
3
4 4 1
3
2 1 1
3
3 1 2
3
4 3 2
3
3 2 4
3
4 2 3
3
1 1 1
3
3 4 2
3
3 3 2
3
1 2 1
3
2 2 4
3
3 1 3
3
1 2 3
2
4 4
3
3 3 3
3
2 1 3
3
3 2 1
3
1 3 3
3
4 2 2
3
3 1 4
3
2 3 4
3
2 4 3
3
1 2 2
3
3 3 1
3
1 4 4
3
1 3 2
2
3 3
3
2 3 2
3
4 1 3
3
2 2 2
3
2 2 3
3
4 3 1
3
3 2 3
3
3 4 1
3
2 2 1
2
1 1
3
2 4 2

*/

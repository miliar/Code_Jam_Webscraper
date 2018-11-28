#include<bits/stdtr1c++.h>
using namespace std;
typedef long long LL;


int main()
{
    #ifndef ONLINE_JUDGE
        freopen("2.in","r",stdin);
		freopen("2.out","w",stdout);
    #endif // ONLINE_JUDGE
    
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int r,c,w;
    int tc;
    cin>>tc;
    int ic=1;
    while(tc--)
    {
    	cin>>r>>c>>w;
    	int ret=0;
    	int acc[2]={1,w};
    	int d=1;
    	if(w==1)
    		ret=r*c;
    	else{
    	for(int i=0;i<r-1;i++)
    		for(int j=w;j<=c;j+=w){d=!d; ret++;}

    	for(int j=w;j<c;j+=w){d=!d; ret++;}
    	ret+=w;
    	}
    	cout<<"Case #"<<ic++<<": ";
    	cout<<ret<<endl;

    }




    return 0;
    
}

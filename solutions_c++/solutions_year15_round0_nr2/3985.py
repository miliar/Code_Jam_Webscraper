#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int main(){


    int t,n,mx2,mn2,min1;
    freopen("output.txt","w",stdout);
    freopen("input.txt","r",stdin);
	scanf("%d",&t);
	
	int count = 0;

    while(t--){

        count++;
        scanf("%d",&n);

        int a[n+1];
        mx2 = 0;
        for(int i=0;i<n; i++)
        {
            cin>>a[i];
            mx2 = max(mx2,a[i]);
        }

        mn2 = mx2;
         min1 = 0;

        for(int i=1 ; i <= mx2; i++)
		{
        min1=i;
        for(int j=0;j<n;j++){
        if(a[j]>i){
        if( a[j]%i == 0 ){
        min1 += (a[j]/i -1);
        }
        else{
        min1 += (a[j]/i);
        }
        }
        }
        mn2 =min(mn2,min1);
        }
        cout<<"Case #"<<count<<": "<<mn2<<endl;
    }
    return 0;
}


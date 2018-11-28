#include<iostream>
#include<cstdio>
using namespace std;

main(){
    freopen("B-amall.in","r",stdin);
   freopen("B-amall.out","w",stdout);
    int testcase,N;
    cin>>testcase;
    for(N=1;N<=testcase;N++){
        int temp,i,j,c,n,m,r,max=-1,min=1000,can=1;
        cin>>n>>m;
        int array[n][m];
        for(i=0;i<n;i++)
            for(j=0;j<m;j++){
                cin>>array[i][j];
                if(array[i][j]<min)
                    min=array[i][j];
                if(array[i][j]>max)
                    max=array[i][j];
            }
    for(i=min;i<max;i++){
        for(j=0;j<n;j++){
            for(temp=0;temp<m;temp++){
                if(array[j][temp]==i){
                    //check
                    for(r=0;r<n;r++)
                        {
                            if(array[r][temp]!=i)
                            {
                                for(c=0;c<m;c++)
                                    if(array[j][c]!=i)
                                        {
                                            can=0;
                                            goto end;
                                        }
                            }
                        }
                }
            }
        }
    }
    end:
     cout<<"Case #"<<N<<": ";
     if(can) cout<<"YES\n";
     else cout<<"NO\n";
    }
}

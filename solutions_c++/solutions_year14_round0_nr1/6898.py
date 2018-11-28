#include <iostream>
#include<cstdio>
#include <string>

using namespace std;
#define len 4
#define ll long long int
#define in(a) scanf("%d",&a);

int main()
{
    int first[len][len],sec[len][len];
    int ans1,ans2,t,c;
    in(t);
    int ans[100],k=0,res;
    while(t--){
        in(ans1);
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++)
                in(first[i][j]);
        }
        in(ans2);
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++)
                in(sec[i][j]);
        }
        c=0;res=0;
        for(int i=0;i<4;i++){
                for(int j=0;j<4;j++){
                        if(first[ans1-1][i]==sec[ans2-1][j]){res=first[ans1-1][i];c++;}
                }
        }
        if(c==1)ans[k]=res;
        else if(c>1)ans[k]=-1;
        else ans[k]=0;
        k++;
    }
    for(int i=0;i<k;i++){
        if(ans[i]==-1)printf("Case #%d: Bad magician!\n",i+1);
        else if(ans[i]==0)printf("Case #%d: Volunteer cheated!\n",i+1);
        else  printf("Case #%d: %d\n",i+1,ans[i]);
    }
	return 0;
}

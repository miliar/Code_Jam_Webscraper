#include<bits/stdc++.h>
using namespace std;
char m[300][300];
int n[300][300];
inline char mul(char x,char y,int &neg){
    neg^=n[x][y];
    return m[x][y];
}
main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("pC.txt","w",stdout);
    m['1']['1']=m['i']['i']=m['j']['j']=m['k']['k']='1',m['1']['i']=m['i']['1']=m['j']['k']=m['k']['j']='i';
    m['1']['j']=m['j']['1']=m['i']['k']=m['k']['i']='j',m['1']['k']=m['k']['1']=m['i']['j']=m['j']['i']='k';
    n['i']['i']=n['j']['j']=n['k']['k']=n['i']['k']=n['j']['i']=n['k']['j']=1;
    int T,p=1;
    scanf("%d",&T);
    while(T--){
        char small[100000],str[100000]={0},val='1';
        int i,ans=0,n,m;
        scanf("%d %d %s",&n,&m,small);
        for(i=0;i<m;i++)strcat(str,small);
        int len=strlen(str),fail=1,neg=0;
        for(i=0;i<len;i++){
            val=mul(val,str[i],neg);
            if(val=='i'&&neg==0){
                fail=0;
                break;
            }
        }
        if(fail)printf("Case #%d: NO\n",p++);
        else{
            val='1',fail=1,neg=0;
            for(i++;i<len;i++){
                val=mul(val,str[i],neg);
                if(val=='j'&&neg==0){
                    fail=0;
                    break;
                }
            }
            if(fail)printf("Case #%d: NO\n",p++);
            else{
                val='1',fail=1,neg=0;
                for(i++;i<len;i++){
                    val=mul(val,str[i],neg);
                }
                if(val!='k'||neg==1)printf("Case #%d: NO\n",p++);
                else printf("Case #%d: YES\n",p++);
            }
        }
    }
    return 0;
}

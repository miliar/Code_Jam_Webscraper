#include<iostream>
#include<cstdio>
#include<set>
#include<cstring>

using namespace std;

char a[109];

void flip(int pos){

    for(;pos>0;--pos)
        if(a[pos]=='+')
            a[pos]='-';
        else 
            a[pos]='+';

}

int main(){
	
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    
    int t;
    scanf("%d",&t);

    for(int tt=1;tt<=t;++tt){
        
    
        scanf("%s",a+1);

        int len=strlen(a+1),ans=0;


        for(int i=len;i>0;--i){

            if(a[i]=='+')
                continue;
            
            ++ans;
            flip(i-1);
            

        }
        printf("Case #%d: %d\n",tt,ans);

    }

    return 0;


}

#include <bits/stdc++.h>
using namespace std;
int main() {
        #ifndef ONLINE_JUDGE
    	freopen("inp.txt","r",stdin);
    	freopen("out.txt","w",stdout);
    #endif	
	int t,i,j,len,s,v,f1,o,h,e,n,k=1;
        char str[2005];
        cin>>t;
        while(t--){
                s=0;v=0;o=0;f1=0,n=0,e=0,h=0;
               int  f[10]={0};
                cin>>str;
                len=strlen(str);
                for(i=0;i<len;i++){
                        if(str[i]=='Z'){
                               f[0]+=1;
                                }
                        if(str[i]=='V')
                                v++;
                        if(str[i]=='F')
                                f1++;
                        if(str[i]=='H')
                                h++;
                        if(str[i]=='E')
                                e++;
                        if(str[i]=='N')
                                n++;
                        if(str[i]=='O')
                                o++;
                        if(str[i]=='W')
                              f[2]+=1;
                        if(str[i]=='U')
                                f[4]+=1;
                        if(str[i]=='X')
                                f[6]+=1;
                        if(str[i]=='G')
                                f[8]+=1;
                        if(str[i]=='S')
                                s++;
                      }
                if(f[0]){
                        o-=f[0];
                        }
                if(f[2]){
                        o-=f[2];
                        }
                if(f[4]) o-=f[4];
                if(o)  f[1]+=o;
                
                if(f[4]){
                        f1-=f[4];
                        }
             if(f1) f[5]+=f1;
                
                if(f[5]) v-=f[5];
                if(v)   f[7]+=v;

               if(f[1]) n-=f[1];
                if(f[7]) n-=f[7];
                if(n)  f[9]+=n/2;
             
                if(f[8]) h-=f[8];
                if(h) f[3]+=h;
                
             cout<<"Case #"<<k++<<": ";
                for(i=0;i<10;i++){
                        if(f[i]>1){
                                cout<< i;
                                f[i]-=1;
                                i--;
                        }
                        else if(f[i]==1)
                                cout<<i;
                }       
                  cout<<endl;
                }
                                    
return 0;       
}

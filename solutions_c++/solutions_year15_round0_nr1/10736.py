#include<bits/stdc++.h>
using namespace std;

int main()
{
    long long m,t,i,tot=0,v=0,kiwi=1;
    int d;
   // FILE *f=fopen("A-small-attempt0.in","r");
   // FILE *g=fopen("outit.txt","w");
  //  fscanf(f,"%lld\n",&t); 
  ifstream f;
  f.open("A-small-attempt3.in");
  ofstream g;
  g.open("outit.txt");
    char s[1000]; char x[2];
    f>>t;
   do
   {
    t--;
    tot=0; v=0;
    //fscanf(f,"%lld %s\n",&m,s);
    f>>m>>s;
   cout<<m<<" "<<s<<endl;
    for(i=0;i<=m;i++)
    {   x[0]=s[i];
        x[1]='\0';
        d=atoi(x);
        
        
        if(d!=0 && tot<i)
        {
            v+=abs(i-tot); 
            tot+=(v+d);  
        }
        else tot+=d;
    
    }
      // fprintf(g,"%s%d%s%d%c","Case #",kiwi,": ",v,'\n');
      g<<"Case #"<<kiwi<<": "<<v<<"\n";
      cout<<" "<<v<<endl;
        kiwi++;
    }while(t!=0);
    return 0;
}
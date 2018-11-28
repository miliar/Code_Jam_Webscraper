#include<iostream>
#include<fstream>
using namespace std;
int main(){
    int count =0;
    int a,b,c,d,e,f,g;
    int x,y,z,v;
    int test;
    int value;
    int indication=0;
    int cases=0;
    ifstream fin("inn.txt");
     ofstream fout("o.txt");
    
    fin>>test;
    for(int i=0 ; i< test ; i++)
    {
fin>>e;

for(int t=1 ; t<=e ; t++)
{
        fin>>a>>b>>c>>d;
      //  cout<<a<<b<<c<<d;
    //    cout<<"\n";
        }//
            
int r=4-e;
for(int l=0 ; l<r; l++ )
{fin>>x>>y>>z>>v;}

fin>>f;
for(int hh=0; hh<f ; hh++)
{
     fin>>x>>y>>z>>v;
    // cout<<x<<y<<z<<v;
    // cout<<"\n";
     }
   if(a==x || a== y || a== z || a ==v ){count++; value=a;indication ++; }  
     if(b==x || b== y || b== z || b ==v ){count++;value=b;indication ++;}
     if(c==x || c== y || c== z || c ==v ){count++;value=c;indication ++;}
     if(d==x || d== y || d== z || d ==v ){count++;value=d;indication ++;}
 
if(count==1 && indication ==1){fout <<"Case #"<<++cases<<": "<<value<<"\n";}
 if(count >1){fout <<"Case #"<<++cases<<": "<<"Bad magician!"<<"\n";}
 else if(count ==0){fout <<"Case #"<<++cases<<": "<<"Volunteer cheated!"<<"\n";}
     
     
int rr=4-f;
for(int ll=0;ll<rr;ll++)
{fin>>x>>y>>z>>v;}
     

count=0;indication=0;
}
fout.close();
 //   cout<<"asd";
cin.get();    
}

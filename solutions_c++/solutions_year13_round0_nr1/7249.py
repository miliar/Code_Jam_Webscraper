#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
int t,i,j,k=1;
cin>>t;
while(t--)
{
    cout<<"Case #"<<k<<": ";
    k++;
    vector<string>a(4);
    for(i=0;i<4;i++)
    cin>>a[i];
    
vector<int>xrow(4,0),xcol(4,0),orow(4,0),ocol(4,0);
int dots=0,xcount=0,ocount=0,diglx=0,digrx=0,digro=0,diglo=0;
int j;

for(i=0;i<4;i++)
for(j=0;j<4;j++)
{
                if(i==j)
                {
                        if(a[i][j]=='T')
                        {
                        digrx++;digro++;
                        }
                        if(a[i][j]=='X')
                        digrx++;
                        if(a[i][j]=='O')
                        digro++;
                }
                if(i+j==3)
                {
                          if(a[i][j]=='T')
                          {diglx++;diglo++;
                          }
                          
                          if(a[i][j]=='X')
                        diglx++;
                          if(a[i][j]=='O')      
                        diglo++;
                }
                if(a[i][j]=='T')
                {
                        xrow[i]++;
                        xcol[j]++;
                        orow[i]++;
                        ocol[j]++;        
                        xcount=max(xcount,max(xrow[i],xcol[j]));
                        ocount=max(ocount,max(orow[i],ocol[j]));
                } 
                else if(a[i][j]=='X')
                {    
                     xrow[i]++;
                     xcol[j]++;
                     xcount=max(xcount,max(xrow[i],xcol[j]));        
                }
                else   if(a[i][j]=='O')
                {
                       orow[i]++;
                       ocol[j]++;
                       ocount=max(ocount,max(orow[i],ocol[j]));
                }
                else
                {
                 dots++;          
                }
}
if(xcount==4||digrx==4||diglx==4)
{
cout<<"X won"<<endl;
continue;
}
else
if(ocount==4||digro==4||diglo==4)
{
cout<<"O won"<<endl;
continue;
}
else if(dots==0)
{
cout<<"Draw"<<endl;    
}
else
{
    cout<<"Game has not completed"<<endl;
}
}
}

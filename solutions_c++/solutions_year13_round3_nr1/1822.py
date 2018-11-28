#include <iostream>
#include <map>
#include <set>

using namespace std;


bool contiguo(string &line, int &n)
{
bool toReturn=false;
int cont=0;
for(int i=0;i<line.size();++i)
{
    if((line[i]=='a') ||(line[i]=='e') ||(line[i]=='i') ||(line[i]=='o') ||(line[i]=='u'))
    {
        cont=0;
    }
    else
    {
        cont++;
        if(cont == n)
            return true;
    }
}

return false;

}

int main()
{
 int cases;
 cin>>cases;

 for(int c=1;c<=cases;++c)
 {
 string line;
 string temp;
 int n;
 cin>>line>>n;
 int cont=0;


 for(int l=1;l<=line.size();++l)
 {
     for(int s=0;s<line.size();++s)
     {
         temp = line.substr(s,l);


         if(temp.size()==l)
         {
         //cout<<temp<<" "<<temp.size()<<" "<<l<<" ";
         if(contiguo(temp,n))
         {

            cont++;
           // cout<<"true"<<endl;

         }
         }

     }
 }

 cout<<"Case #"<<c<<": "<<cont<<endl;




 }


return 0;
}

#include<iostream>
#include<vector>
#include<fstream>
using namespace std;
int main()
{
    FILE* in ;
    in= fopen("input.txt", "r");
    ofstream fpo;
    fpo.open("output.txt");
    int T;
//    cin>>T;
      fscanf(in, "%d", &T);
    int ct=1;
    for(;ct<=T;++ct)
    {
         int ri, rf;
         vector<int> vi;          
         vector<int> vf;
         
         int a[4][4];
         int b[4][4];
//         cin>> ri;
      fscanf(in, "%d", &ri);
         int i,j;
         
         for(i=0;i<4;++i)
         {
           for(j=0;j<4;++j)
           {
                           int d;
                         //  cin>>d;
                         fscanf(in, "%d", &d);
                           a[i][j]=d;
           }                
         }
         
//         cin>>rf;
           fscanf(in, "%d", &rf);
         for(i=0;i<4;++i)
         {
           for(j=0;j<4;++j)
           {
                           int d;
//                           cin>>d;
                              fscanf(in, "%d", &d);
                           b[i][j]=d;
           }                
		 }
         
       int count=0;
       for ( ;count<4; ++count)
       {
           vi.push_back(a[ri-1][count]);
           vf.push_back(b[rf-1][count]);
       }
  
 int cans=0;
 int vans;
   vector<int>:: iterator it1, it2;
   for(it1= vi.begin(); it1!=vi.end(); ++it1)
   {
               for(it2= vf.begin(); it2!=vf.end(); ++it2)
                if(*it1== *it2)
                {
                   cans++;
                   if(cans==1)
                        vans= *it1;
                }
   }
         
         //cout<< "Case #" << ct<<": ";
         fpo<< "Case #" << ct<<": ";
         if(cans==1)
         {
//           cout<<vans<<endl;
             fpo<<vans<<endl;
                      
         }
         else if (cans>1)
//         cout<< "Bad magician!\n";
         fpo<< "Bad magician!\n";
         else
         fpo << "Volunteer cheated!\n";
              
    }
    fpo.close();
    fclose(in);
 system("pause");
 return 0;   
}

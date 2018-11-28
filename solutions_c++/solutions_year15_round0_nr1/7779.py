#include<iostream>
#include<fstream>
#include<string>
#include<vector>
using namespace std;

#define loop(i,j,k) for(int i = j; i < k; i++)
#define foreach(i,v) for(int i = 0; i < v.size(); i++)





int main()
{
    int T;
    ofstream f;
    f.open("output.txt",ios::out);
    cin >> T;
    loop(i,0,T)
    {
          int n;
          cin >> n;
          string str;
          cin >> str;
          
          vector<int> v;
          int res = 0;
          foreach(j, str)
          {
              int num = str[j] - '0';
              v.push_back(num);       
                              
          }
          int max = 0;
          
          loop(j, 0, (v.size()))
          {
                if ( v[j] == 0 )
                   continue;
                if (max < j)
                   { 
                     res += j - max;
                     //cout <<j<< "::"<<max<<endl;
                     max += v[j] + j - max;
                   }
                else
                 max += v[j];
                              
          }
          
          f << "Case #" << i +1 <<": "<<res <<endl;
          
    
          
             
    
    
    }
    f.close();
    //getchar();getchar();
    
    return 0;
}

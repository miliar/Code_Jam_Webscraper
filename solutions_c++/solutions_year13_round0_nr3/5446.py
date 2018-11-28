#include<iostream>
#include<math.h>
#include<string.h>
#include<vector>
#include<fstream>
using namespace std;
vector<int> v;
int main()
{
    //ifstream fin;
    ofstream fout;
    fout.open("F://codejam3.txt");
    int t,a,b,i=1,cnt=0;
    std::cin>>t;
    while(t)
    {
        std::cin>>a;
        std::cin>>b;
       if(1>=a && 1<=b) cnt++;
       if(4>=a && 4<=b) cnt++;
       if(9>=a && 9<=b) cnt++;
       if(121>=a && 121<=b) cnt++;
       if(484>=a && 484<=b) cnt++;
        fout<<"Case #"<<i<<": "<<cnt<<"\n";
        //v.push_back(cnt);
        --t;
        i++;
        cnt=0;

    }
    fout.close();
    //for(i=0;i<v.size();i++)


}

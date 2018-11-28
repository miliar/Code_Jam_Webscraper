#include<iostream>
#include<fstream>
#include<vector>
using namespace std;
int main()
{
    int t,n,j;
    ifstream in("C:\\Users\\Abhi\\Downloads\\A-large.in");
    ofstream out("C:\\Users\\Abhi\\Downloads\\A-large.out");
    bool flag = false;
    vector<int>dig;
    in>>t;
    int i;
    for(i=0;i<t;++i){
        in>>n;
        if(!n){
            out<<"Case #"<<i+1<<": INSOMNIA"<<endl;
            continue;
        }
        flag = false;
        for(j=1;flag == false;++j){
            int k;
            int temp = j*n;
            while(temp){
                for(k=0;k<dig.size() && dig[k]!=temp%10;++k);
                if(k==dig.size())
                    dig.push_back(temp%10);
                if(dig.size() == 10){
                    out<<"Case #"<<i+1<<": "<<j*n<<endl;
                    flag = true;
                    break;
                }
                temp/=10;
            }
        }
        dig.clear();
    }
}

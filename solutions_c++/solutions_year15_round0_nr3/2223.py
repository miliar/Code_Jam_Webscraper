#include <iostream>
#include <fstream>
#include <cassert>
#include <cctype>
#include <vector>
#include <algorithm>
#include <cstdlib>

using namespace std;



int main()
{
    fstream in,out;
    in.open("small.in",fstream::in);
    out.open("small.out",fstream::out|fstream::app);
    int mulchart[4][4] = {{1,2,3,4},{-2,-1,4,-3},{3,-4,-1,2},{4,3,-2,-1}};
    int num;
    in >> num;
    for(int i = 0;i != num; ++i)
    {
        int l = 0, x=0;
        in >> l >>x;
        char c;
        vector<int> str{};
        for(int i=0;i!=l;++i)
        {
            in>>c;
            switch (c){
                case 'i':str.push_back(2);break;
                case 'j':str.push_back(3);break;
                case 'k':str.push_back(4);break;
            }
        }
            int target=2,sum=1;
            for(int j=0;j!=x;++j)
            {
                for(auto k=str.begin();k!=str.end();++k)
                {
                    int temp=*k;
                    bool sign = sum>0?true:false;
                    sum = mulchart[abs(sum)-1][temp-1];
                    if(!sign) sum=-sum;
                    if(sum==target)
                    {++target;sum=1;}

                }
            }
        bool rlt=false;
        if(target==5&&sum==1) rlt=true;
        out << "Case #" << i+1 << ": ";
        if(rlt) out<< "Yes" <<endl;
        else out<<"No"<<endl;

    }
    return 0;
}

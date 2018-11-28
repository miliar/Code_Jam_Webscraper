#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main()
{
    fstream fin,fout;
    fin.open("B-large.in",ios::in);
    fout.open("out.txt",ios::out);
    int t,m;
    fin>>t;
    m=t;
    while(t--)
    {
        string str;
        fin>>str;
        vector<int>bit_string,tmp;
        int i,at=0,sum=0;
        for(i=0;i<str.size();++i)
            if(str[i]=='+') tmp.push_back(1);
            else tmp.push_back(0);
        while(at<str.size())
        {
            if(at==0||tmp[at]!=bit_string[bit_string.size()-1]) bit_string.push_back(tmp[at]);
            ++at;
        }
        at=0;
        while(at<bit_string.size())
        {
            if(at==0&&bit_string[at]==0) sum++;
            else if (bit_string[at] == 0)sum += 2;
            at++;
        }
        fout<<"Case #"<<m-t<<": "<<sum<<endl;
    }
    return 0;
}

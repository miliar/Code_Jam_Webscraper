#include <iostream>
#include <fstream>

using namespace std;

ofstream myfile;

void test(int x, string s, int n)
{
    int cnt = (s[0]-'0');
    int tmp = 0;
    for(int i=1; i<=x;i++)
    {
        if(s[i]!='0')
        {
            if(i>cnt )
            {
                tmp +=( i - cnt);
                cnt += (i-cnt);
            }
            cnt += (s[i]-'0');
        }

    }
    myfile << "Case #" << n <<": "<<tmp<<"\n";
}

void rea()
{
    ifstream read("C:\\Users\\Melih\\Desktop\\input.txt");
    int lines,x;
    string s;
    read>>lines;//number of lines
    for(int i=1;i<=lines;i++)
    {
            read>>x>>s;
            test(x,s,i);
    }

}

int main () {
    myfile.open ("C:\\Users\\Melih\\Desktop\\output.txt");
    rea();
    myfile.close();
    return 0;
}

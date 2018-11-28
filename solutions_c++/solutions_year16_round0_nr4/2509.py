#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
    ifstream in("test.txt");
    ofstream out("out.txt");
    if (! in.is_open()){
        cout << "Error opening file";
    }
    int t;
    string s;
    in>>t;
    //vector<int> result;
    int lineCount = 1;
    while(t--){
        int k,c,s;
        in>>k>>c>>s;
        //result.push_back(n);
        out<<"Case #"<<lineCount<<": ";
        for(int i = 1;i<=k;i++)
            out<<" "<<i;
        out<<endl;
        lineCount ++;
    }
    //for(auto ele:result)
    //    out<<ele<<endl;
    in.close();
    out.close();
    return 0;
}

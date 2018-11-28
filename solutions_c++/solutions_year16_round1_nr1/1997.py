#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

string result;

int solve(string& s,string& out){
    for(int i = 0;i<s.size();i++){
        if(out.empty())
            out.push_back(s[i]);
        else{
            string str;
            str.push_back(s[i]);
            if(out + str>str+out)
                out = out + str;
            else
                out = str + out;
        }
    }
    return 0;
}

/*void getSubString(string& s,int index,string currRes){
    if(currRes.length() == s.length())
        if(currRes < result) result = currRes;
}*/

int main()
{
    ifstream in("large.txt");
    ofstream out("largeout.txt");
    if (! in.is_open()){
        cout << "Error opening file";
    }
    int t;
    string s;
    in>>t;
    //vector<int> result;
    int lineCount = 1;
    while(t--){
        in>>s;
        string outstring;
        solve(s,outstring);
        out<<"Case #"<<lineCount<<": "<<outstring<<endl;
        lineCount ++;
    }
    //for(auto ele:result)
    //    out<<ele<<endl;
    in.close();
    out.close();
    return 0;
}

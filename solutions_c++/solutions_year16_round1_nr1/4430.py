#include<bits/stdc++.h>

using namespace std;
//
//string Int_to_string(int number)
//{
//    stringstream ss;
//    ss << number;
//    return ss.str();
//}

int main()
{
    ofstream fs("nombre.txt");
    int T;
    string S;
    cin>>T;

    for(int i=0;i<T;++i)
    {
        cin>>S;
        string res="";
        if(S.size()==1)
            fs<<"Case #"<<i+1<<": "<<S<<endl;
        else
        {
        res+=S[0];
        for(int j=1;j<S.size();++j)
        {
            if((int)S[j]>=(int)res[0])
                res=S[j]+res;
            else
                res=res+S[j];
        }
        fs<<"Case #"<<i+1<<": "<<res<<endl;
        }
    }
    fs.close();
    return 0;
}

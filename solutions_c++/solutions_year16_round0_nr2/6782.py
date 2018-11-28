#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int pancakes(string);

int main()
{
    //ifstream in("large-in.txt");
    //ofstream out("large-out.txt");

    int T;
    string cad;

    cin>>T;
    for(int i=0;i<T;i++){
        cin>>cad;
        cout<<"Case #"<<i+1<<": "<<pancakes(cad)<<endl;
    }
    //in.close();
    //out.close();
    return 0;
}

int pancakes(string s){
    int cont=1;
    int j;

    for(j=1;j<s.size();j++){
        if(s[j-1]!=s[j])
            cont++;
    }
    if('+'==s[s.size()-1])
        cont--;
    return cont;
}

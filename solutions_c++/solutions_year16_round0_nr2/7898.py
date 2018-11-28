#include <iostream>
#include <string>
using namespace std;

int revenge(string s){
    int len = s.size();
    if(len == 0)
        return 0;
    if(len == 1){
        if(s[0] == '+')
            return 0;
        else
            return 1;
    }
    int begins = 0,counts=0;
    char c = s[begins];
    for(int k = 1; k < len; k++){
        if(s[k] != s[begins]){
            c = s[k];
            ++counts;
            begins = k;
        }
        if(k == len-1){
            if(c =='-')
                return ++counts;
            else
                return counts;
        }
    }
}


int main()
{

    freopen("E:\\code_jam\\problemB\\Revenge of the Pancakes\\B-large.in","r",stdin);
    freopen("E:\\code_jam\\problemB\\Revenge of the Pancakes\\test.txt","w",stdout);
    int sums=0;
    cin>>sums;
    string s;
    int k =1;
    while(k<=sums){
        int result = 0;
        cin>>s;
        result = revenge(s);
        cout<<"Case #"<<k<<": "<<result<<endl;
        ++k;
    }
    fclose(stdin);
    fclose(stdout);


    return 0;
}

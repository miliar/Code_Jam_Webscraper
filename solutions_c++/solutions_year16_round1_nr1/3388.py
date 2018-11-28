#include <iostream>
#include <list>
using namespace std;


void ans(int index){
    list<char> name;
    string in;
    getline(cin,in);
    for(int i=0;i<in.length();i++){
        if(name.size()==0){
            name.push_back(in[i]);
        }
        else if(in[i]>=name.front())
            name.push_front(in[i]);
        else name.push_back(in[i]);
    }

    cout<<"Case #"<<index<<": ";
    list<char>::const_iterator iterator;
    for (iterator = name.begin(); iterator != name.end(); ++iterator) {
        std::cout << *iterator;
    }
    cout  << std::endl;
}

int main(int argc, char const *argv[]) {
    int t;
    cin>>t;
    cin.ignore();
    for(int i=0;i<t;i++){
        ans(i+1);
    }
    return 0;
}

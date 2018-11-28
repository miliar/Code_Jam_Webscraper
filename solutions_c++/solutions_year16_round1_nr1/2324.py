#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <queue>
#include <string>


using namespace std;

#define true 1
#define false 0

priority_queue<string> words;

void lastWords(priority_queue<string> &words, string original, int idx, string current){
    //cout<<"original: "<<original<< " index: "<<idx<<" current: "<<current<<endl;
    // string front(current);
    // string back(current);
    string letter (original, idx, 1);
    if(current.length()==original.length()){
        words.push(current);
        //cout<<current<<endl;
    } else {
        // cout<<"back: "<<back<<endl;
        // back.push_back(original[idx]);
        // cout<<"back: "<<back<<endl;
        //cout<<"current+letter: "<<(current+letter)<<endl;
        //string newword = current+letter;
        lastWords(words, original, idx+1, current+letter);
        // front.insert(front.begin(), original[idx]);
        // cout<<"front: "<<front<<endl;
        lastWords(words, original, idx+1, (letter+current));
    }
}

int main(){
    int cases;
    scanf("%d", &cases);
    getchar();
    for(int n=1; n<=cases; ++n){
        string str;
        cin>>str;
        //cout<<"string: "<<str<<endl;
        priority_queue<string> words;
        //if(words.empty())   cout<<"===>vazia"<<endl;
        string first (str, 0, 1);
        //cout<<"first: "<<first<<"."<<endl;
        lastWords(words, str, 1, first);
        cout<<"Case #"<<n<<": ";//<<lastWord(str)<<endl;
        cout<<words.top()<<endl;
    }
    
    
    return 0;
}
#include<iostream>
#include<string>

using namespace std;

string lastword(string word)
{
    int length= word.length();
    string last_word;
    last_word = word[0];
    for(int i=1; i<length; i++)
    {
        if(word[i]>=last_word[0])
        {
            last_word=word[i]+last_word;
        }
        else
        {
            last_word=last_word+word[i];
        }
    }
    return last_word;
}


int main()
{
    int no_of_case;
    cin >> no_of_case;
    for(int i=0; i<no_of_case; i++)
    {
        string word;
        cin >> word;
        string last_word;
        last_word = lastword(word);
        cout<< "Case #"<<i+1<<":"<<" "<<last_word<<'\n';
    }
    return 0;
}

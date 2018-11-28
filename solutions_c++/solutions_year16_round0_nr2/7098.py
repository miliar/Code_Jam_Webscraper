#include<iostream>
using namespace std;

int main()
{
    int times;
    cin>>times;
	int times_ori=times;
    cin.ignore();
    string input;
    int i, count;
    while(times--)
    {
        count=1;
        getline(cin, input);
        for(i=1;i<input.length();i++) if( (input[i-1]=='+' && input[i]=='-') || (input[i-1]=='-' && input[i]=='+') ) count++;
        if(input[input.length()-1]=='+') count--;
        cout<<"Case #"<<times_ori-times<<": "<<count<<endl;

    }
    return 0;
}

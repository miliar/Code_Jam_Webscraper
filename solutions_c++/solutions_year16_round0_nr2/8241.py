#include <iostream>

using namespace std;

int main()
{
    int T, count=0;
    string input;
    cin>>T;
    for(int z=0; z<T; z++){
        cin>>input;
        for(int i=0; i<input.length(); i++){
            for(int j=i+1; j<input.length(); j++){
                if(input[i] != input[j]){
                    for(int p=i; p<j; p++){
                        input[p] = input[j];
                    }
                    count++;
                }
            }
        }
        if(input[0] == '-')
            count++;
        cout<<"Case #"<<z+1<<": "<<count<<endl;
        count = 0;
    }
    return 0;
}

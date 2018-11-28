#include <iostream>

using namespace std;

int main()
{
    int T;
    cin >>T;

    for(int c=1; c<=T; c++){

        string str;
        int smax;
        cin>>smax>>str;

        int min_friend = 0;

        int num_standing = 0;

        for(int i=0; i<str.size(); i++){

            int tmp = str[i] - '0';

            if(num_standing >= i){

                num_standing += tmp;
            } else {

                min_friend += i - num_standing;

                num_standing += tmp + i - num_standing;
            }


        }


        cout<<"Case #"<<c<<": "<< min_friend<<endl;
    }
    return 0;
}


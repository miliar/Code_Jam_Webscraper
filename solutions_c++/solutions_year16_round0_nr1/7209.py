#include<iostream>
#include<fstream>
#include<string>
#include<deque>
#include<stack>
#include<map>
#include<set>

using namespace std;

int main(){

    ofstream myfile;
    myfile.open ("output.in");

    long long int T;
    cin>>T;

    for(long long int case_i = 1 ; case_i<=T ; case_i++){

        long long int arr[10] = {1,2,3,4,5,6,7,8,9,0};
        long long int iterations = 0;

        set<long long int> elements;
        elements.insert(arr,arr+10);

        long long int input;
        cin>>input;

        long long int lastNumber = 0;
        long long int N = 1;

        long long int oldbignum[100000] = {0};
        long long int numend = 0;

        long long int temp = input;
        long long int oldindex = 0;

        bool found = false;
        while(temp != 0){
            int last = temp % 10;

            oldbignum [oldindex++] = last;
            elements.erase(last);

            if(elements.empty()){
                found = true;
                lastNumber = input;
            }

            temp = temp / 10;
        }

        if(found){
            cout<<"Case #"<<case_i<<": "<<input<<endl;
            myfile<<"Case #"<<case_i<<": "<<input<<endl;
        }

        while(!found)
        {
            if(input == 0){
                break;
            }

            long long int bignum[100000] = {0};
            long long int index = oldindex;

            for(long long int i = 0 ; i<oldindex ; i++){
                bignum [i] = oldbignum[i];
            }

            long long int carry = 0;
            for(long long int i=0;i<index;i++){
                long long int num = bignum [i]*N + carry;
                long long int last = num % 10;

                bignum [i] = last;
                elements.erase(last);

                if(elements.empty()){
                    found = true;
                }

                carry = num / 10;
            }

            long long int temp = input;
            while(carry != 0){
                long long int last = carry % 10;

                bignum [index++] = last;
                elements.erase(last);

                if(elements.empty()){
                    found = true;
                }

                carry = carry / 10;
            }
//
//            cout<<"\nnext big num : ";
//            for(int i=index - 1;i >= 0;i--){
//                cout<<bignum [i];
//            }
//
//            cout<<"    elements left : ";
//            for (std::set<int>::iterator it=elements.begin(); it!=elements.end(); ++it)
//                std::cout << ' ' << *it;

            if(found){

                cout<<"Case #"<<case_i<<": ";
                for(long long int i=index - 1;i >= 0;i--){
                    cout<<bignum [i];
                }
                cout<<endl;

                myfile<<"Case #"<<case_i<<": ";
                for(long long int i=index - 1;i >= 0;i--){
                    myfile<<bignum [i];
                }
                myfile<<endl;

                break;
            }

            N++;
            iterations++;
            if(iterations > 100000){
                break;
            }
        }

        if(!found){
                cout<<"Case #"<<case_i<<": INSOMNIA"<<endl;
                myfile<<"Case #"<<case_i<<": INSOMNIA"<<endl;
            }
    }

    return 0;
}

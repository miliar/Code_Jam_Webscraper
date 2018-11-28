#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char* argv[])    {

    int first_guess = 0;
    int second_guess = 0;
    int first_array[4];
    int second_array[4];
    int tmp;

    int cases; cin>>cases;
    for(int x=1;x<=cases;x++)  {

        cin>>first_guess;
        for(int i=0;i<4;i++)    {
            for(int j=0;j<4;j++)    {
                cin>>tmp;
                if(i+1==first_guess)    {
                    first_array[j] = tmp;;
                }
            }
        }

        cin>>second_guess;
        for(int i=0;i<4;i++)    {
            for(int j=0;j<4;j++)    {
                cin>>tmp;
                if(i+1==second_guess)   {
                    second_array[j] = tmp;;
                }
            }
        }

        vector<int> ret;
        for(int i=0;i<4;i++)    {
            for(int j=0;j<4;j++)    {
                if(first_array[i]==second_array[j]) {
                    ret.push_back(first_array[i]);
                }
            }
        }

        cout<<"Case #"<<x<<": ";
        int size = ret.size();
        if(size==0) {
            cout<<"Volunteer cheated!"<<endl;
        }else if(size>1)    {
            cout<<"Bad magician!"<<endl;
        }else  {
            cout<<ret[0]<<endl;;
        }
    }
    return 0;
}
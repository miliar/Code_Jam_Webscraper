#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(){
        int T;
        string temp;
        cin>>T;
        vector<string> pancakeStacks;
        for (int i=0;i<T;i++){
                cin >> temp;
                pancakeStacks.push_back(temp);
        }
        for (int i=0;i<T;i++){
                int flips=0;
                string pancakeStack = pancakeStacks[i];
                bool flipped = false;
                for (int j=pancakeStack.length()-1;j>=0;j--){
                        if ((pancakeStack[j]=='-') && !flipped){
                                flips++;
                                flipped=true;
                        }
                        else if ((pancakeStack[j]=='+') && flipped){
                                flips++;
                                flipped=false;
                        }
                }
                cout << "Case #"<<(i+1)<<": "<<flips<<endl;
        }
}

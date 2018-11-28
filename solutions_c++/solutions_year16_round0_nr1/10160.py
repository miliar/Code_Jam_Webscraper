#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<unordered_set>
#include <fstream>


using namespace std;
void countSheep(int num,int i){
    unordered_set<int> set;
    unordered_set<int> duplicate;
    ofstream myfile;
    myfile.open("myfile.txt", std::ios::app);
    int temp1=num;
    while(true){
        int temp2=num;
        if(duplicate.count(temp2)!=0) {
            
            myfile<<"Case #"<<i<<": INSOMNIA"<<endl;
            myfile.close();
            return;
        }else{
            duplicate.insert(temp2);
        }
        while(num>0){
            set.insert(num%10);
            num/=10;
            if(set.size()==10){
                myfile<<"Case #"<<i<<": "<<temp2<<endl;
                myfile.close();
                return;
            }
        }
        num=temp2+temp1;
    }
    
}
int main()
{
    int num = 0;
    cin>> num;
    for(int i=1;i<=num;i++){
        int input;
        cin>>input;
        countSheep(input,i);
    }
    return 0;
}
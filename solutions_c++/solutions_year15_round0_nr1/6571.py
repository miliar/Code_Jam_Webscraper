#include<iostream>
inline int char2int(char c){
    return c-'0';
}
int main(){
    int tests;
    std::cin>>tests;
    for(int kh = 0; kh!=tests;++kh){
        int max_shy;
        std::cin >> max_shy;
        std::string in;
        std::cin >> in;

        int standing_count = 0;
        int friends=0;
        for(int i = 0; i!=in.size();++i){
            if(in.at(i)=='0'){continue;}
            if(!(standing_count >= i)){
                friends+=i-standing_count;
                standing_count+=i-standing_count;
            }
            standing_count+=char2int(in.at(i));

        }
        std::cout << "Case #" << kh+1 << ": " << friends << std::endl;
    }


}

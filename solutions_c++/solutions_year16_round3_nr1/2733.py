#include <list>
#include <vector>
#include <iostream>
#include <fstream>

class Party{
    public:
    int num;
    char name;
    Party(int n, char c){
        num = n;
        name = c;
    }
};

bool compare(const Party& pt1, const Party& pt2){
    return pt1.num>pt2.num||(pt1.num == pt2.num&&pt1.name<pt2.name);
}

int main(int argc, char*argv[]){
    std::ifstream istr(argv[1]);
    char arr[26] = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
    int cases, pt_num, ppl_num;
    istr >> cases;
    int case_num = 1;
    while (istr >> pt_num){
        int i = 0;
        float total = 0;
        std::list<Party> pt_list;
        while(i<pt_num){
            istr >> ppl_num;
            pt_list.push_back(Party(ppl_num, arr[i]));
            total += ppl_num;
            ++i;
        }
        std::cout << "Case #"<<case_num<<": ";
        pt_list.sort(compare);

        while (pt_list.size()){
                (*pt_list.begin()).num -= 1;
                total -= 1;
                std::cout <<(*pt_list.begin()).name;
                if ((*pt_list.begin()).num == 0){
                    pt_list.pop_front();
                    if (pt_list.size() == 0)
                    break;
                }
                pt_list.sort(compare);
                if ((*pt_list.begin()).num/total>0.5){
                    (*pt_list.begin()).num -= 1;
                    total -=1;
                    std::cout <<(*pt_list.begin()).name;
                    if ((*pt_list.begin()).num == 0){
                        pt_list.pop_front();
                    }
                    pt_list.sort(compare);
                }
            std::cout<<" ";
        }
        std::cout << std::endl;
        case_num += 1;
    }
    return 0;
}
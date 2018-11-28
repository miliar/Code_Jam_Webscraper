/*
** Author: Pan Tianxiang 
** Email: ptx9363<dot>gmail.com
** Created at: 2015-04-11 22:46:25
*/


#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;


int get_shyness_level_persons(string raw, int** shyest_persons){
    int blank = raw.find(' ');
    
    int max_shyness_level = atoi(raw.substr(0, blank).c_str());
    *shyest_persons = new int[max_shyness_level + 1];
    for(int i = 0; i <= max_shyness_level; i++){
        (*shyest_persons)[i] = atoi(raw.substr(blank+i+1, 1).c_str());
    }
    
    return max_shyness_level;
}

int calculate_frends(int max_shyness_level, int* shyest_persons){
    int friends_need_invite = 0;
    int standed_persons = shyest_persons[0];
    for(int i = 1; i <= max_shyness_level; i++){
        if (standed_persons < i){
            friends_need_invite += i - standed_persons;
            standed_persons = i;
        }
        standed_persons += shyest_persons[i];
    }
    return friends_need_invite;
}

int main(){
    
    int test_cases_number;

    cin >> test_cases_number;
    
    for(int i = 0; i < test_cases_number; i++){
        
        string raw = "";
        while(raw == "")
            getline(cin, raw);

        int max_shyness_level;
        int* shyest_persons;
        
        max_shyness_level = get_shyness_level_persons(raw, &shyest_persons);

        int friends_need_invite = calculate_frends(max_shyness_level, shyest_persons);
        
        delete shyest_persons;

        cout << "Case #" << i+1 << ": " << friends_need_invite << endl; 
    }


    return 0;
}

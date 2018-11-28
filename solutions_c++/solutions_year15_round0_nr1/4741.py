#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int solve();

int num_cases;
int max_shyness;
string shy_array;
ifstream fs("input.txt", ifstream::in);
ofstream ofs("output.txt");

int main() {
    fs >> num_cases;
    for(int i=0;i<num_cases;++i) {
        fs >> max_shyness;
        fs >> shy_array;
        ofs << "Case #" << i + 1 << ": " << solve() << "\n";
//        std::cerr << "2333\n";
    }
    return 0;
}

int people_at_level(int i) {
    return shy_array[i] - '0';
}

int solve() {
    int current_standing = 0;
    int smallest_slot = 0;
    int invited = 0;
    for(int i=0;i<=max_shyness;++i) {
        if(people_at_level(i) != 0) {
            while(current_standing < i) {
                //we try to invite some people
                auto invite_cur_level = min(i - current_standing, 9 - people_at_level(smallest_slot));
                invited += invite_cur_level;
                current_standing += invite_cur_level;
                ++smallest_slot;
            }
            current_standing += people_at_level(i);
        }
//        std::cerr << current_standing << "\n";
    }
    return invited;
}

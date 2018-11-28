#include <cassert>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>

int main() {
    std::ifstream fin("A.in");
    std::ofstream fout("A.out");

    assert (fin.is_open());

    int T;
    fin >> T;

    for (int case_number = 1; case_number <= T; ++case_number) {
        int s_max;
        fin >> s_max;

        int running_total = 0;
        int invites = 0;

        std::string s_string;
        fin >> s_string;
        assert (s_string.size() == s_max + 1);
        for (int s_index = 0; s_index <= s_max; ++s_index) {
            char s_i_char = s_string[s_index];
            int s_i = atoi(&s_i_char);
            int invited = 0;
            if (s_index > running_total && s_i > 0) {
                invited = (s_index - running_total);
                invites += invited;
            }
            running_total += invited + s_i;
        }
        assert (invites >= 0);
        fout << "Case #" << case_number << ": " << invites << std::endl;
    }
    fin.close();
    fout.close();
}



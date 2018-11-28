#include <iostream>
#include <map>

int main()
{
    int T;

    std::cin >> T;

    for (int idx = 1; idx <= T; idx ++)
    {
        std::map<char, int> letters;
        int numbers[10] = {0};
        std::string coded_phone;

        std::cin >> coded_phone;

        for (int i = 0; i < coded_phone.size(); i++) {
            letters[coded_phone[i]]++;
        }

        numbers[0] = letters['Z'];
        letters['Z'] -= numbers[0];
        letters['E'] -= numbers[0];
        letters['R'] -= numbers[0];
        letters['O'] -= numbers[0];

        numbers[2] = letters['W'];
        letters['T'] -= numbers[2];
        letters['W'] -= numbers[2];
        letters['O'] -= numbers[2];

        numbers[6] = letters['X'];
        letters['S'] -= numbers[6];
        letters['I'] -= numbers[6];
        letters['X'] -= numbers[6];

        numbers[7] = letters['S'];
        letters['S'] -= numbers[7];
        letters['E'] -= numbers[7];
        letters['V'] -= numbers[7];
        letters['E'] -= numbers[7];
        letters['N'] -= numbers[7];

        numbers[5] = letters['V'];
        letters['F'] -= numbers[5];
        letters['I'] -= numbers[5];
        letters['V'] -= numbers[5];
        letters['E'] -= numbers[5];

        numbers[4] = letters['F'];
        letters['F'] -= numbers[4];
        letters['O'] -= numbers[4];
        letters['U'] -= numbers[4];
        letters['R'] -= numbers[4];

        numbers[3] = letters['R'];
        letters['T'] -= numbers[3];
        letters['H'] -= numbers[3];
        letters['R'] -= numbers[3];
        letters['E'] -= numbers[3];
        letters['E'] -= numbers[3];

        numbers[8] = letters['H'];
        letters['E'] -= numbers[8];
        letters['I'] -= numbers[8];
        letters['G'] -= numbers[8];
        letters['H'] -= numbers[8];
        letters['T'] -= numbers[8];

        numbers[1] = letters['O'];
        letters['O'] -= numbers[1];
        letters['N'] -= numbers[1];
        letters['E'] -= numbers[1];

        numbers[9] = letters['I'];
     
        std::cout << "Case #" << idx << ": ";
        for (int i = 0; i < 10; i++) {
            for (int j =0; j < numbers[i]; j++) {
                std::cout << i;
            }
        }
        std::cout << std::endl;
    }

    return 0;
}

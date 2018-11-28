#include <cstdio>
#include <fstream>
#include <iostream>
#include <cstring>

using namespace std;

int main()
{

    ifstream in;
    in.open("A-large.in");
    ofstream out;
    out.open("out.txt");

    int case_num;
    in >> case_num;

    for (int i_case = 1; i_case <= case_num; i_case++)
    {

        string s;
        in >> s;
        int len = s.length();
        bool is_used[len];
        for (int i = 0; i < len; i++) {is_used[i] = false;}
        int digits[10];
        for (int i = 0; i < 10; i++) {digits[i] = 0;}

        for (int i = 0; i < len; i++) //first round
        {

            if ((s[i] == 'Z')&&(is_used[i] == false)) //ZERO
            {
                digits[0]++;
                is_used[i] = true;
                for(int j = 0; j < len; j++)
                    if((s[j] == 'E')&&(is_used[j] == false)) {is_used[j] = true; break;}
                for(int j = 0; j < len; j++)
                    if((s[j] == 'R')&&(is_used[j] == false)) {is_used[j] = true; break;}
                for(int j = 0; j < len; j++)
                    if((s[j] == 'O')&&(is_used[j] == false)) {is_used[j] = true; break;}
            }

            if ((s[i] == 'W')&&(is_used[i] == false)) //TWO
            {
                digits[2]++;
                is_used[i] = true;
                for(int j = 0; j < len; j++)
                    if((s[j] == 'T')&&(is_used[j] == false)) {is_used[j] = true; break;}
                for(int j = 0; j < len; j++)
                    if((s[j] == 'O')&&(is_used[j] == false)) {is_used[j] = true; break;}
            }

            if ((s[i] == 'U')&&(is_used[i] == false)) //FOUR
            {
                digits[4]++;
                is_used[i] = true;
                for(int j = 0; j < len; j++)
                    if((s[j] == 'F')&&(is_used[j] == false)) {is_used[j] = true; break;}
                for(int j = 0; j < len; j++)
                    if((s[j] == 'O')&&(is_used[j] == false)) {is_used[j] = true; break;}
                for(int j = 0; j < len; j++)
                    if((s[j] == 'R')&&(is_used[j] == false)) {is_used[j] = true; break;}
            }

            if ((s[i] == 'X')&&(is_used[i] == false)) //SIX
            {
                digits[6]++;
                is_used[i] = true;
                for(int j = 0; j < len; j++)
                    if((s[j] == 'I')&&(is_used[j] == false)) {is_used[j] = true; break;}
                for(int j = 0; j < len; j++)
                    if((s[j] == 'S')&&(is_used[j] == false)) {is_used[j] = true; break;}
            }

            if ((s[i] == 'G')&&(is_used[i] == false)) //EIGHT
            {
                digits[8]++;
                is_used[i] = true;
                for(int j = 0; j < len; j++)
                    if((s[j] == 'E')&&(is_used[j] == false)) {is_used[j] = true; break;}
                for(int j = 0; j < len; j++)
                    if((s[j] == 'I')&&(is_used[j] == false)) {is_used[j] = true; break;}
                for(int j = 0; j < len; j++)
                    if((s[j] == 'H')&&(is_used[j] == false)) {is_used[j] = true; break;}
                for(int j = 0; j < len; j++)
                    if((s[j] == 'T')&&(is_used[j] == false)) {is_used[j] = true; break;}
            }

        }

        for (int i = 0; i < len; i++) //second round
        {

            if ((s[i] == 'O')&&(is_used[i] == false)) //ONE
            {
                digits[1]++;
                is_used[i] = true;
                for(int j = 0; j < len; j++)
                    if((s[j] == 'N')&&(is_used[j] == false)) {is_used[j] = true; break;}
                for(int j = 0; j < len; j++)
                    if((s[j] == 'E')&&(is_used[j] == false)) {is_used[j] = true; break;}
            }

            if ((s[i] == 'R')&&(is_used[i] == false)) //THREE
            {
                digits[3]++;
                is_used[i] = true;
                for(int j = 0; j < len; j++)
                    if((s[j] == 'T')&&(is_used[j] == false)) {is_used[j] = true; break;}
                for(int j = 0; j < len; j++)
                    if((s[j] == 'H')&&(is_used[j] == false)) {is_used[j] = true; break;}
                for(int j = 0; j < len; j++)
                    if((s[j] == 'E')&&(is_used[j] == false)) {is_used[j] = true; break;}
                for(int j = 0; j < len; j++)
                    if((s[j] == 'E')&&(is_used[j] == false)) {is_used[j] = true; break;}
            }

            if ((s[i] == 'F')&&(is_used[i] == false)) //FIVE
            {
                digits[5]++;
                is_used[i] = true;
                for(int j = 0; j < len; j++)
                    if((s[j] == 'I')&&(is_used[j] == false)) {is_used[j] = true; break;}
                for(int j = 0; j < len; j++)
                    if((s[j] == 'V')&&(is_used[j] == false)) {is_used[j] = true; break;}
                for(int j = 0; j < len; j++)
                    if((s[j] == 'E')&&(is_used[j] == false)) {is_used[j] = true; break;}
            }

            if ((s[i] == 'S')&&(is_used[i] == false)) //SEVEN
            {
                digits[7]++;
                is_used[i] = true;
                for(int j = 0; j < len; j++)
                    if((s[j] == 'E')&&(is_used[j] == false)) {is_used[j] = true; break;}
                for(int j = 0; j < len; j++)
                    if((s[j] == 'V')&&(is_used[j] == false)) {is_used[j] = true; break;}
                for(int j = 0; j < len; j++)
                    if((s[j] == 'E')&&(is_used[j] == false)) {is_used[j] = true; break;}
                for(int j = 0; j < len; j++)
                    if((s[j] == 'N')&&(is_used[j] == false)) {is_used[j] = true; break;}
            }

        }

        for (int i = 0; i < len; i++) //third round
        {
            if ((s[i] == 'N')&&(is_used[i] == false)) //ONE
            {
                digits[9]++;
                is_used[i] = true;
                for(int j = 0; j < len; j++)
                    if((s[j] == 'I')&&(is_used[j] == false)) {is_used[j] = true; break;}
                for(int j = 0; j < len; j++)
                    if((s[j] == 'N')&&(is_used[j] == false)) {is_used[j] = true; break;}
                for(int j = 0; j < len; j++)
                    if((s[j] == 'E')&&(is_used[j] == false)) {is_used[j] = true; break;}
            }
        }


        //out
        out << "Case #" << i_case << ": ";
        for (int i = 0; i < 10; i++)
        {
            for (int j = 0; j < digits[i]; j++)
                out << i;
        }
        out << endl;




//        if (insomnia)
//            out << "Case #" << i_case << ": INSOMNIA" << endl;
//        else
//            out << "Case #" << i_case << ": " << current_num << endl;
//        //out << endl;

    }

    in.close();
    out.close();

    return 0;

}

#include <cstdio>
#include <fstream>
#include <iostream>
#include <cstring>

using namespace std;

bool is_dig_arr_full(string dig_arr);

int main()
{

    ifstream in;
    in.open("in.txt");
    ofstream out;
    out.open("out.txt");

    int case_num;
    in >> case_num;

    for (int i_case = 1; i_case <= case_num; i_case++)
    {

        int num;
        in >> num;

        string dig_arr ("aaaaaaaaaa");
        bool insomnia = false;

        if (num == 0)
        {
            dig_arr = "0123456789";
            insomnia = true;
        }

        int current_num = 0;
        while (!is_dig_arr_full(dig_arr))
        {
            current_num += num;
            string str_num = to_string(current_num);
            for (int i = 0; i < str_num.length(); i++)
                switch(str_num[i])
                {
                    case '0': dig_arr[0] = '0';
                              break;
                    case '1': dig_arr[1] = '1';
                              break;
                    case '2': dig_arr[2] = '2';
                              break;
                    case '3': dig_arr[3] = '3';
                              break;
                    case '4': dig_arr[4] = '4';
                              break;
                    case '5': dig_arr[5] = '5';
                              break;
                    case '6': dig_arr[6] = '6';
                              break;
                    case '7': dig_arr[7] = '7';
                              break;
                    case '8': dig_arr[8] = '8';
                              break;
                    case '9': dig_arr[9] = '9';
                              break;
                    default:
                        cout << "default" << endl;
                }
            //out << current_num << " " << dig_arr << endl;
        }

        if (insomnia)
            out << "Case #" << i_case << ": INSOMNIA" << endl;
        else
            out << "Case #" << i_case << ": " << current_num << endl;
        //out << endl;

    }

    in.close();
    out.close();

    return 0;

}

bool is_dig_arr_full(string dig_arr)
{
    return dig_arr == "0123456789";
}

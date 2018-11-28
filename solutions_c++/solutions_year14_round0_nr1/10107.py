#include<iostream>
#include<fstream>
#include<cstring>

using namespace std;

int string_parser(char *str);
void switch_out(int case_val, int input_case,int default_val=0);
int* strarray_parser(char* str, int* line);
int compare(int* first, int* second, int input_case);

int string_parser(char *str)
{
    int num = 0;
    int len = 0;

    cout<<"parsing "<<str<<" \n";
    for(len=0; str[len] != '\0';len++);

    for(int j=0; j<len; j++)
    {
        num = (num*10) + (str[j] - '0');
    }

    return num;
}

void switch_out(int case_val, int input_case,int default_val)
{
    ofstream outfile;

    cout <<"Case value :"<<case_val<<" input :"<<input_case<<" value :"<<default_val<<endl;
    outfile.open("out.txt",ios::out|ios::app);

    switch(case_val)
    {
    case 1:
        {
            outfile<<"Case #"<<input_case<<": "<<default_val<<endl;
        }
        break;
    case 2:
        {
            outfile<<"Case #"<<input_case<<": Bad magician!"<<endl;
        }
        break;
    case 3:
        {
            outfile<<"Case #"<<input_case<<": Volunteer cheated!"<<endl;
        }
        break;
    }
}

int* strarray_parser(char* str, int* line)
{
    int temp = 0;
    int index = 0;

    cout<<"Parsing string : "<<str<<endl;
    for(unsigned int i=0; i <= strlen(str); i++)
    {
        if((str[i] == ' ')||(str[i] == '\0'))
        {
            cout<<"\n"<<temp<<endl;
            line[index++] = temp;
            temp = 0;
        }
        else
        {
            temp = (temp*10) + (str[i] - '0');
        }
    }
    return line;
}

int compare(int* first, int* second, int input_case)
{
    int flag = 0;
    int super_flag = 0;
    int sub_flag = 0;
    int default_value = 0;

    cout<<"Comparing :"<<first[0]<<" "<<first[1]<<" "<<first[2]<<" "<<first[3]<<"  "<<second[0]<<" "<<second[1]<<" "<<second[2]<<" "<<second[3]<<" Case :"<<input_case<<endl;
    for(int i=0; i<4; i++)
    {
        for(int j=0; j<4; j++)
        {
            if(first[i] == second[j])
            {
                if(flag == 1)
                {
                    super_flag = 1;
                    break;
                }
                flag = 1;
                sub_flag = 0;
                default_value = first[i];
            }
            else
            {
                sub_flag = 1;
            }
        }
    }
    if(flag >= 0)
    {
        if((flag == 1) && (super_flag == 0))
        {
            switch_out(1,input_case,default_value);
        }
        else if((flag == 1) && (super_flag == 1))
        {
            switch_out(2,input_case);
        }
        else if(sub_flag == 1)
        {
            switch_out(3,input_case);
        }

        return 1;
    }
    else
    {
        return 0;
    }
}

int main()
{
    int *card;
    int *card2;
    int choice = 0;
    int tot_input = 0;

    ifstream infile;

    infile.open("A-small-attempt0.in",ios::in);

    card = new int[4];
    card2 = new int[4];

    char* str = new char[10];
    infile.getline(str,10,'\n');
    tot_input = string_parser(str);
    delete[] str;

    for(int i = 0;i<tot_input;i++)
    {
        for(int j=0; j<2; j++)
        {
            char* str1 = new char[10];
            infile.getline(str1,10,'\n');
            choice = string_parser(str1);
            delete[] str1;

            for(int k=0; k<4; k++)
            {
                char* str2 = new char[20];
                infile.getline(str2,15,'\n');
                if((k+1) == choice)
                {
                    if(j == 0)
                    {
                        card = strarray_parser(str2,card);
                    }
                    else if(j == 1)
                    {
                        card2 = strarray_parser(str2,card2);
                    }
                    delete[] str2;
                }
                else
                {
                    delete[] str2;
                }
            }
        }
        if(compare(card,card2,i+1))
        {
            cout<<"Executed "<<i+1<<" input to file\n";
        }
        else
        {
            cout<<"Error in execution of "<<i+1<<" input\n";
        }
    }

    return 0;
}

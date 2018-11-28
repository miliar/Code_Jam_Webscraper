#include <iostream>
#include <string>
#include <vector>

bool checkStack(std::vector<bool> stack){

    for (auto v : stack)
    {
        if (v == false)
        {
            return false;
        }
    }

    return true;
}

std::vector<bool> toBoolVector(std::string s){
    std::vector<bool> output;
    for (auto side : s)
    {
        output.push_back ((side == '+') ? true : false );
    }

    return output;
}

int getIdx(std::vector<bool> stack){
    std::vector<bool> input_data(stack);
    if (input_data.size() == 1) {
        return 0;
    }

    for (int i = 0; i < input_data.size(); i++)
    {
        if (i != input_data.size()-1 && i+1 <= input_data.size())
        {
            if (input_data[i] != input_data[i+1])
            {
                return i;
            }
        }else{
            return i;
        }
    }

    return -1;
}

std::vector<bool> flip(std::vector<bool> stack){
    int idx = getIdx(stack);
    std::vector<bool> output(stack);
    for (int i = 0; i < idx+1; i++)
    {
        output[i].flip();
    }

    return output;
}

int main(int argc, char* argv[])
{
    std::vector<bool> stack;

    int j = 0;
    int i = 0;
    std::string n;
    while (std::cin >> n && j < 101)
    {
        stack = toBoolVector(n);
        while (!checkStack(stack))
        {
            if(j==0)break;
            stack = flip(stack);
            i++;
        }

        if(j!=0)
        {
            std::cout << "Case #" << j << ": " << i << std::endl;
        }

        i = 0;
        j++;
        stack.clear();
    }

    return 0;
}

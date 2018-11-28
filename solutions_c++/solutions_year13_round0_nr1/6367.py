#include <iostream>
#include<string>
char check_win(std::string& row);
int main()
{
    int test_cases;
    std::cin >> test_cases;
    //std::cin.ignore();
    for (int i=0;i<test_cases;++i){
        bool cont = true;
        int removed = 0;
        bool is_there_dot=false;
        std::string diagonal_left; std::string diagonal_right;
        std::string one; std::string two;std::string three;std::string four;
        std::cout<<"Case #"<<(i+1)<<": ";
        for (int j=0;j<4;++j){
                std::string line;
                std::cin>> line;
                ++removed;
                if (check_win(line)=='X'){
                    //std::cout<<"horizontal wins"<<std::endl;
                    std::cout << "X won"<<std::endl;
                    cont = false;
                    break;
                }
                else if (check_win(line)=='O'){
                    //std::cout<<"horizontal wins"<<std::endl;
                    std::cout << "O won"<<std::endl;
                    cont = false;
                    break;
                }
                if (!is_there_dot){
                    if (!(line.find('.')==std::string::npos)){
                        is_there_dot = true;
                    }
                }
                if (j==3){
                        //append the last characters
                        one += line[0]; two += line[1]; three += line[2]; four += line[3];
                        diagonal_left += line[j]; diagonal_right += line[3-j];
                        //std::cout<<"["<<line<<"]"<<std::endl;
                        //std::cout<<"("<<one<<")"<<std::endl;
                        //one
                        if (check_win(one)=='X'){
                            std::cout << "X won"<<std::endl;
                            cont = false;
                            break;
                        }
                        else if (check_win(one)=='O'){
                            std::cout << "O won"<<std::endl;
                            cont = false;
                            break;
                        }
                        //two
                        if (check_win(two)=='X'){
                            std::cout << "X won"<<std::endl;
                            cont = false;
                            break;
                        }
                        else if (check_win(two)=='O'){
                            std::cout << "O won"<<std::endl;
                            cont = false;
                            break;
                        }
                        //three
                        if (check_win(three)=='X'){
                            std::cout << "X won"<<std::endl;
                            cont = false;
                            break;
                        }
                        else if (check_win(three)=='O'){
                            std::cout << "O won"<<std::endl;
                            cont = false;
                            break;
                        }
                        //four
                        if (check_win(four)=='X'){
                            std::cout << "X won"<<std::endl;
                            cont = false;
                            break;
                        }
                        else if (check_win(four)=='O'){
                            std::cout << "O won"<<std::endl;
                            cont = false;
                            break;
                        }
                        //diagonal_left
                        if (check_win(diagonal_left)=='X'){
                            std::cout << "X won"<<std::endl;
                            cont = false;
                            break;
                        }
                        else if (check_win(diagonal_left)=='O'){
                            std::cout << "O won"<<std::endl;
                            cont = false;
                            break;
                        }
                        //diagonal_right
                        if (check_win(diagonal_right)=='X'){
                            std::cout << "X won"<<std::endl;
                            cont = false;
                            break;
                        }
                        else if (check_win(diagonal_right)=='O'){
                            std::cout << "O won"<<std::endl;
                            cont = false;
                            break;
                        }
                    }
                    else{
                        //append characters to columns
                        one += line[0]; two += line[1]; three += line[2]; four += line[3];
                        diagonal_left += line[j]; diagonal_right += line[3-j];
                        ///std::cout<<"["<<line<<"]"<<std::endl;
                       // std::cout<<"("<<one<<")"<<std::endl;
                    }
                }
        if (cont){
            //if there was no win and there is a dot on the grid, the game is not finished
            if (is_there_dot){
                std::cout << "Game has not completed"<<std::endl;
            }
            else{
                std::cout << "Draw"<<std::endl;
            }
        }
        std::string tmp_line;
        for (int i=0;i<4-removed;++i){
            std::cin>>tmp_line;
        }
}
return 0;
}
char check_win(std::string& row){
    unsigned int string_size = row.size();
    std::string tmp = std::string(row);
    //check X win
    unsigned found = tmp.find_first_of("XXXT");
    while(found<string_size){
        tmp[found] = 'z';
        found =tmp.find_first_of("XXXT", found+1);
    }
    if (tmp == "zzzz"){
        return 'X';
    }
    //check O
    tmp = row;
    found = tmp.find_first_of("OOOT");
    while(found<string_size){
        tmp[found] = 'z';
        found =tmp.find_first_of("OOOT", found+1);
    }
    if (tmp == "zzzz"){
        return 'O';
    }
    return 'N';
}

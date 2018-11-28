#include <iostream>
#include <set>
#include <algorithm>

using namespace std;

struct CaseTest
{
    int answer[2];
    int number1[16];
    int number2[16];
};

void process(CaseTest&, int);

int main()
{
    int nbCase;
    cin >> nbCase;

    CaseTest* input = new CaseTest[nbCase];

    for(int i=0 ; i<nbCase ; ++i)
    {
        cin >> input[i].answer[0];
        for(size_t j=0 ; j<16 ; ++j)
            cin >> input[i].number1[j];

        cin >> input[i].answer[1];
        for(size_t j=0 ; j<16 ; ++j)
            cin >> input[i].number2[j];
    }

    for(int i=0 ; i<nbCase ; ++i)
    {
        process(input[i], i);
    }

    delete[] input;
    return 0;
}



void process(CaseTest& ct, int index)
{
    set<int> set1, set2, diff;

    set1.insert(ct.number1+(ct.answer[0]-1)*4, ct.number1+(ct.answer[0]-1)*4+4);
    set2.insert(ct.number2+(ct.answer[1]-1)*4, ct.number2+(ct.answer[1]-1)*4+4);
    std::set_intersection(set1.begin(), set1.end(), set2.begin(), set2.end(),
                        std::inserter(diff, diff.end()));
    if(diff.size() == 1)
    {
        cout << "Case #"<<index+1<<": "<<*(diff.begin())<<endl;
    }
    else if(diff.empty())
    {
        cout << "Case #"<<index+1<<": Volunteer cheated!"<<endl;
    }
    else
    {
        cout << "Case #"<<index+1<<": Bad magician!"<<endl;
    }
}

/*******************************************************************************
    Copyright (C) 2014-2016 Wright State University - All Rights Reserved
    Daniel P. Foose - Maintainer/Lead Developer

    This file is part of Vespucci.

    Vespucci is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Vespucci is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Vespucci.  If not, see <http://www.gnu.org/licenses/>.
*******************************************************************************/
#include <iostream>
#include <fstream>
#include <cstdint>
#include <map>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

class DigitTracker{
public:
    DigitTracker();
    bool DigitTracked(uint digit);
    bool AllDigitsTracked();
    void TrackDigit(uint digit);
    void PrintTracked();
private:
    map<uint, bool> digits_;
};

class SheepCounter{
public:
    SheepCounter(uintmax_t first_number);
    uintmax_t GetLastNumber(bool &ok);
    void TestSplitNumber(uint n);
private:
    uintmax_t first_number_;
    DigitTracker tracker_;
    vector<uint> SplitNumber(uintmax_t number);
};

///a function to take powers of uints
/// I read it in a book somewhere
uint UIntPow(uint x, uint p)
{
    if (p == 0) return 1;
    if (p == 1) return x;
    uint val = UIntPow(x, p/2);
    if (p % 2 == 0) return val * val;
    else return x * val * val;
}

int main(int argc, char *argv[])
{
    ifstream input_stream("A-small-attempt0.in");
    vector<uintmax_t> input_data;
    string current_line;

    std::getline(input_stream, current_line);
    uint cases = stoi(current_line);

    while (std::getline(input_stream, current_line)){
        input_data.push_back(stoi(current_line));
    }
    input_stream.close();

    for (uint i = 0; i < cases; ++i){
        SheepCounter counter(input_data[i]);
        bool ok;
        uint last_number = counter.GetLastNumber(ok);
        cout << "Case #" << i + 1 << ": ";
        if (!ok){
            cout << "INSOMNIA" << endl;
        }
        else{
            cout << last_number << endl;
        }
    }

    return 0;
}

DigitTracker::DigitTracker()
{
    for (uintmax_t i = 0; i < 10; ++i)
        digits_.emplace(i, false);
}

bool DigitTracker::DigitTracked(uint digit)
{
    return digits_[digit];
}

bool DigitTracker::AllDigitsTracked()
{
    for (pair<int, bool> digit : digits_)
        if (!digit.second)
            return false;
    return true;
}

void DigitTracker::TrackDigit(uint digit)
{
    digits_[digit] = true;
}

void DigitTracker::PrintTracked()
{
    cout << boolalpha;
    for  (pair<int,bool> digit : digits_)
        cout << digit.first << ": " << digit.second << endl;
}

SheepCounter::SheepCounter(uintmax_t first_number)
{
    first_number_ = first_number;
}

uintmax_t SheepCounter::GetLastNumber(bool &ok)
{
    if (!first_number_){
        ok = false;
        return 0;
    }
    //track digits in first number
    vector<uint> digits = SplitNumber(first_number_);
    for (uint digit : digits)
        tracker_.TrackDigit(digit);

    uint i = 2;
    uintmax_t current_number = first_number_;
    while (!tracker_.AllDigitsTracked()){
        current_number = i * first_number_;
        //if overflow
        if (current_number == UINTMAX_MAX){
            ok = false;
            return current_number;
        }
        vector<uint> digits = SplitNumber(current_number);
        for (uint digit : digits)
            tracker_.TrackDigit(digit);

        ++i;
    }

    ok = true;
    return current_number;
}

void SheepCounter::TestSplitNumber(uint n)
{
    vector<uint> digits = SplitNumber(n);
    cout << "n = " << n;
    cout << "digits ";
    for (uint digit : digits){
        cout << digit << " ";
    }
    cout << endl;
}

vector<uint> SheepCounter::SplitNumber(uintmax_t number)
{
    //log10(number) must exist, so number cannot be 0
    uint n_digits = log10(number) + 1;
    vector<uint> digits;
    for (uint i = 1; i <= n_digits; ++i){
        uint current_digit = (number % UIntPow(10, i)) / UIntPow(10, i-1);
        digits.push_back(current_digit);
    }
    return digits;
}

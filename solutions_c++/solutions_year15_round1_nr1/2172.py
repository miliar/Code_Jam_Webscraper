#include <EatManager.hpp>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;
//------------------------------------------------------------------------------
void EatManager::init()
{
    cin >> mCount;

    for (int i = 0; i < mCount; ++i) {
        cin >> mPlates[i];
    }

    mMethod1 = 0;
    mMethod2 = 0;
}

//------------------------------------------------------------------------------
void EatManager::calc()
{
    //method1
    {
        for (int i = 0; i < mCount - 1; ++i) {
            int eatCount = mPlates[i] - mPlates[i+1];
            if (eatCount > 0) {
                mMethod1 += eatCount;
            }
        }
    }

    //method2
    {
        // 最大差を探す
        int diffMax = 0;
        for (int i = 0; i < mCount - 1; ++i) {
            int diff = mPlates[i] - mPlates[i+1];
            if (diff > diffMax) {
                diffMax = diff;
            }
        }

        for (int i = 0; i < mCount - 1; ++i) {
            int eatCount = mPlates[i];
            if (eatCount > diffMax) {
                eatCount = diffMax;
            }
            if (eatCount > 0) {
                mMethod2 += eatCount;
            }
        }
    }
}

//------------------------------------------------------------------------------
void EatManager::dump() const
{
    cout << "count: " << mCount << endl;
    for (int i = 0; i < mCount; ++i) {
        cout << mPlates[i] << " ";
    }
    cout << endl;
}

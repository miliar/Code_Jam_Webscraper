// ================================================================================================
//  D - Ominous Omino.cpp
//  Written by Luis Garcia, 2015
// ================================================================================================

#include <cstdio>
#include <cassert>
#include <cstring>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <iterator>
#include <numeric>
#include <iostream>

using namespace std;

#if defined _OJ_PROJECT
_BEGIN_PROBLEM(_GCJ15_01D, "GCJ15 01D")
#endif // _OJ_PROJECT

#define infinite_loop for (;;)

bool tryPieces(const vector<vector<int>> & forcedPieces, const vector<vector<int>> & otherPieces, vector<int> & map, const vector<int> & filled, bool forced = false) {
    if (forced && map == filled)
        return true;

    for (auto piece : (!forced ? forcedPieces : otherPieces)) {
        assert(piece.size() == map.size());
        bool valid = true;
        for (int i = 0; i < map.size(); ++i)
            valid &= (piece[i] & map[i]) == 0;
        if (!valid) continue;

        for (int i = 0; i < map.size(); ++i) map[i] |= piece[i];
        if (tryPieces(forcedPieces, otherPieces, map, filled, true)) return true;
        for (int i = 0; i < map.size(); ++i) map[i] &= ~piece[i];
    }
    return false;
}

void addTranslations(const vector<vector<bool>> & piece, vector<vector<int>> & output, int H, int W, int R, int C) {
    vector<int> processedPiece(R);
    for (int i = 0; i < H; ++i)
        for (int j = 0; j < W; ++j)
            if (piece[i][j])
                processedPiece[i] |= (1 << j);

    for (int i = 0; i <= R - H; ++i)
        for (int j = 0; j <= C - W; ++j) {
            vector<int> pieceForm(R);
            for (int k = 0; k < H; ++k)
                pieceForm[k + i] = (processedPiece[k] << j);
            output.push_back(pieceForm);
        }
}

void addReflections(vector<vector<bool>> piece, vector<vector<int>> & output, int H, int W, int R, int C) {
    addTranslations(piece, output, H, W, R, C);
    
    for (int i = 0; i < H; ++i)
        for (int j = 0, k = W - 1; j < k; ++j, --k)
            swap(piece[i][j], piece[i][k]);

    addTranslations(piece, output, H, W, R, C);

    for (int j = 0, k = H - 1; j < k; ++j, --k)
        for (int i = 0; i < W; ++i)
            swap(piece[j][i], piece[k][i]);

    addTranslations(piece, output, H, W, R, C);

    for (int i = 0; i < H; ++i)
        for (int j = 0, k = W - 1; j < k; ++j, --k)
            swap(piece[i][j], piece[i][k]);

    addTranslations(piece, output, H, W, R, C);
}

void createPieceForms(const vector<string> & piece, int R, int C, vector<vector<int>> & pieceForms) {
    vector<vector<bool>> rawPieceForm(R, vector<bool>(C)),
                         rawPieceForm90(R, vector<bool>(C));

    int H = piece.size(), W = piece[0].size();

    if (H <= R && W <= C) {
        for (int i = 0; i < H; ++i)
            for (int j = 0; j < W; ++j)
                if (piece[i][j] == 'x')
                    rawPieceForm[i][j] = true;
        addReflections(rawPieceForm, pieceForms, H, W, R, C);
    }

    if (W <= R && H <= C) {
        for (int i = 0; i < H; ++i)
            for (int j = 0; j < W; ++j)
                if (piece[i][j] == 'x')
                    rawPieceForm90[j][i] = true;
        addReflections(rawPieceForm90, pieceForms, W, H, R, C);
    }
}

bool canBeCompleted(const vector<string> & forcedPiece, const vector<vector<string>> & pieces, int R, int C) {
    vector<vector<int>> forcedPieceForms, otherPieceForms;

    createPieceForms(forcedPiece, R, C, forcedPieceForms);
    sort(forcedPieceForms.begin(), forcedPieceForms.end());
    forcedPieceForms.erase(unique(forcedPieceForms.begin(), forcedPieceForms.end()), forcedPieceForms.end());

    for (auto piece : pieces)
        createPieceForms(piece, R, C, otherPieceForms);
    sort(otherPieceForms.begin(), otherPieceForms.end());
    otherPieceForms.erase(unique(otherPieceForms.begin(), otherPieceForms.end()), otherPieceForms.end());

    vector<int> map(R), filled(R, (1 << C) - 1);
    return tryPieces(forcedPieceForms, otherPieceForms, map, filled);
}

int main() {
    vector<vector<vector<string>>> pieces = {
        {},
        {{"x"}},
        {{"xx"}},
        {{"xxx"}, {"xx", "x."}},
        {{"xxxx"}, {"xxx", "x.."}, {"xx", "xx"}, {"xxx", ".x."}, {"xx.", ".xx"}},
    };

    int T, X, R, C;
    scanf("%d", &T);
    for (int _T = 1; _T <= T; ++_T) {
        scanf("%d %d %d", &X, &R, &C);

        bool answer = true;
        if (R * C % X != 0)
            answer = false;
        else
            for (auto piece : pieces[X])
                answer &= canBeCompleted(piece, pieces[X], R, C);

        printf("Case #%d: %s\n", _T, answer ? "GABRIEL" : "RICHARD");
    }

    return 0;
}

#if defined _OJ_PROJECT
_END_PROBLEM
#endif // _OJ_PROJECT

// ================================================================================================
//  End of file.
// ================================================================================================
